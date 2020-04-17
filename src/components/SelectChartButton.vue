<template>

    <v-dialog v-model="dialog" persistent max-width="1000px">
        <template v-slot:activator="{ on }">

            <v-btn icon v-on="on">
                <v-icon>mdi-wrench</v-icon>
            </v-btn>
        </template>
        <v-card>
            <v-card-title>
                <span class="headline">Configure Pane</span>
            </v-card-title>
            <v-card-text>
                <v-container>
                    <v-row>
                        <v-col>
                            <v-text-field label="Title*" type="text" required></v-text-field>
                            <v-select
                                    v-model="selection"
                                    :items="chartTypes"
                                    label="Select a type*"
                                    required
                            ></v-select>
                            <v-row align="center"
                                   justify="center" v-if="selection.search('Chart')!==-1 ">
                                <v-file-input v-model="file" type="file" label="File input" outlined dense/>
                                <xlsx-read :file="file">
                                    <xlsx-json @parsed="getCollection"/>
                                </xlsx-read>
                                <h1 class="pb-6 px-6">-OR-</h1>
                                <v-text-field disabled outlined dense label="Add your json data array"
                                              v-model="jsonDataTyped"/>
                            </v-row>
                            <v-row v-if="selection.search('html')!==-1">
                                <v-text-field outlined label="Enter Html"></v-text-field>
                            </v-row>
                            <v-row v-if="selection.search('picture')!==-1">
                                <v-text-field outlined label="Enter image url"></v-text-field>
                            </v-row>
                            <v-row v-if="selection.search('text')!==-1">
                                <v-textarea outlined label="Enter text"></v-textarea>
                            </v-row>
                        </v-col>
                    </v-row>
                </v-container>
                <small>*indicates required field</small>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color=" blue darken-1
                            " text @click="closeHandler">Close
                </v-btn>
                <v-btn color="blue darken-1" text @click="closeHandler">Save</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

</template>

<script>
    import Constants from '../assets/constants'
    import XlsxRead from "../../../swe599/node_modules/vue-xlsx/dist/components/XlsxRead";
    import XlsxJson from "../../../swe599/node_modules/vue-xlsx/dist/components/XlsxJson";

    export default {
        components: {
            XlsxRead,
            XlsxJson,

        },


        data: () => ({
            dialog: false,
            selection: '',
            html: '',
            file: null,
            jsonData: [],
            jsonDataTyped: "",
            uploadButton: false,

        }),
        props:['index'],
        methods: {
            getInitialState() {
                this.dialog = false,
                    this.selection = '',
                    this.html = '',
                    this.file = null,
                    this.jsonData = [],
                    this.uploadButton = false

            },

            getCollection(val) {
                if (val)
                    Object.assign(this.jsonData, val)
            },
            closeHandler() {
                if (this.selection.search('Chart') !== -1 && this.file) {
                    const keys=Object.keys(this.jsonData[0])
                    const chartData=this.jsonData.map(e=>e[keys[1]])
                    const chartLabels=this.jsonData.map(e=>e[keys[0]])

                    const componentName=this.selection
                    const index=this.index
                    this.$emit('selections', {componentName,chartData,chartLabels,index})
                }

                this.getInitialState()
            }

        },
        computed: {
            chartTypes() {
                return Constants.chartTypes ? Constants.chartTypes : []
            },
        },
        watch: {}
    }
</script>