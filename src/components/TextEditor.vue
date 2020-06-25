<template>
    <div class="d-flex flex-column justify-content-center mx-3" style="width: 100%,max-width: 600px!important">
        <div>
            <vue-editor style="max-width: 1000px" v-if="saved===false" v-model="content"></vue-editor>
            <div class="container" v-if="saved===true" v-html="content"></div>
        </div>
        <div class="d-flex flex-row justify-end">
            <v-card-actions>
                <v-spacer></v-spacer>

                <v-btn v-if="saved===false" color="blue darken-1" text @click="saveHandler">Save</v-btn>
                <v-btn v-if="saved===true" v-show="!displayForm" color="red darken-1" text @click="saveHandler">Modify</v-btn>
            </v-card-actions>
        </div>

    </div>
</template>

<script>

    import {VueEditor} from "vue2-editor";


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
        methods: {
            saveHandler() {
                this.saved = !this.saved
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
    html body div#app.v-application.v-application--is-ltr.theme--light div.v-application--wrap div#app.pa-8.pb-8 div div.vue-grid-layout div.vue-grid-item.vue-resizable.cssTransforms div.d-flex.flex-column.justify-content-center.mx-3.wrapper.chartComponent div div.container h1 img {
        max-width: 100%!important;
    }

    html body div#app.v-application.v-application--is-ltr.theme--light div.v-dialog__content.v-dialog__content--active div.v-dialog.v-dialog--active.v-dialog--persistent div.v-card.v-sheet.theme--light div.v-card__text div.container div.row div.col div.row div.d-flex.flex-column.justify-content-center.mx-3 div div.container h1 img{
        max-width: 500px!important;
    }
</style>