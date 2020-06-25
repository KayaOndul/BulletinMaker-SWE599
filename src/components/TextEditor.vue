<template>
    <div>
        <vue-editor style="max-width: 1000px" v-model="content"></vue-editor>

    </div>
</template>

<script>

    import {VueEditor} from "vue2-editor";
    import _ from 'lodash'

    const debounceGet = (func) => _.debounce(() => func, 500)

    export default {
        name: 'TextEditor',
        components: {
            VueEditor
        },
        props: ['displayForm', 'insertContent'],
        data() {
            return {
                saved: false,
                content: "<h1>Some initial content</h1>",

            };
        },
        watch: {
            content(newVal) {
                if (newVal) {
                    debounceGet(this.saveHandler)
                }
            }
        },

        methods: {

            saveHandler() {
                console.log('savehandler')
                this.$emit('modified', this.content)
            }
        },
        mounted() {
            this.displayForm ? this.saved = true : this.saved = false
            this.insertContent ? this.content = this.insertContent : this.content = "<h1>Some initial content</h1>"
        }
    };
</script>

<style>



</style>