<template>
    <div class="d-flex flex-column justify-content-center mx-3" style="width: 100%">
        <div>
            <vue-editor v-if="saved===false" v-model="content"></vue-editor>
            <div v-if="saved===true" v-html="content"></div>
        </div>
        <div class="d-flex flex-row justify-end">
            <v-card-actions>
                <v-spacer></v-spacer>

                <v-btn v-if="saved===false" color="blue darken-1" text @click="saveHandler">Save</v-btn>
                <v-btn v-if="saved===true" color="red darken-1" text @click="saveHandler">Modify</v-btn>
            </v-card-actions>
        </div>

    </div>
</template>

<script>

    import { VueEditor } from "vue2-editor";



    export default {
        name: 'TextEditor',
        components: {
            VueEditor
        },

        data() {
            return {
                saved: false,
                content: "<h1>Some initial content</h1>",

            };
        },
        methods: {
            saveHandler() {
                this.saved = !this.saved
                console.log('savehandler')
                this.$emit('modified', this.content)
            }
        }
    };
</script>