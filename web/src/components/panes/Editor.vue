<template>
    <vue-editor class="pb-12" id="editor"
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


        }),
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
