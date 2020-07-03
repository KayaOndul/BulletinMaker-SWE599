<template>
    <vue-editor class="pb-12" id="editor"
                :editor-toolbar="customToolbar"
                useCustomImageHandler
                @image-added="handleImageAdded" v-model="content">
    </vue-editor>

</template>

<script>
    import {VueEditor} from "vue2-editor";


    import helpers from "../../service/helpers";
    import store from "../../store/store";
    import Constants from "../../service/Constants";


    let http = helpers.putToken()

    export default {
        name: 'Editor',
        components: {VueEditor},

        data: () => ({
            content: "",
            iAm: "",
            customToolbar: [
                ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
                ['blockquote', 'code-block'],

                [{'header': 1}, {'header': 2}],               // custom button values
                [{'list': 'ordered'}, {'list': 'bullet'}],
                [{'script': 'sub'}, {'script': 'super'}],      // superscript/subscript
                [{'indent': '-1'}, {'indent': '+1'}],          // outdent/indent
                [{'direction': 'rtl'}],                         // text direction

                [{'size': ['small', false, 'large', 'huge']}],  // custom dropdown
                [{'header': [1, 2, 3, 4, 5, 6, false]}],

                [{'color': []}, {'background': []}],          // dropdown with defaults from theme
                [{'font': []}],
                [{'align': []}],

                ['clean'],                                         // remove formatting button
                ['video']
            ]


        }),
        props: ['GridIndex', 'ReceivedContent'],
        mounted() {
            this.iAm = this.GridIndex
            this.content = this.ReceivedContent
        },


        watch: {
            content(newVal) {
                const iAm = this.iAm
                this.$emit('changed', {newVal, iAm})
            }
        },
        methods: {
            handleImageAdded: function (file, Editor, cursorLocation, resetUploader) {
                console.log('here')
                // An example of using FormData
                // NOTE: Your key could be different such as:
                // formData.append('file', file)

                let formData = new FormData();
                formData.append("file", file);
                store.commit('global/set_loading', true)
                http({
                    url: `${Constants.SERVER_IP}/${Constants.BACKEND_UPLOAD_FILE}`,
                    method: "POST",
                    data: formData
                })
                    .then(result => {
                        let url = `${Constants.SERVER_IP}${result.data.file}`; // Get url from response
                        Editor.insertEmbed(cursorLocation, "image", url);
                        resetUploader();
                        store.commit('global/set_loading', false)
                    })
                    .catch(err => {
                        store.dispatch('global/alertUser', err)
                        console.log(err);
                    });


            }
        }
    };
</script>
