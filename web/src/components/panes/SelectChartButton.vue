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
                            <v-text-field label="Title*" type="text" v-model="title" required></v-text-field>
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
    import Constants from '../../assets/constants'
    import {XlsxJson, XlsxRead} from 'vue-xlsx'

    export default {
        components: {
            XlsxRead,
            XlsxJson,



        },


        data: () => ({
            dialog: false,
            title: '',
            selection: '',
            html: '',
            file: null,
            jsonData: [],
            jsonDataTyped: "",
            pictureURL: "",
            content: '',
            textData: ""


        }),
        props: ['index'],
        methods: {
            getInitialState() {
                this.dialog = false;
                this.selection = '';
                this.html = '';
                this.file = null;
                this.jsonData = [];
                this.pictureURL = "";
                this.title = '';
                this.textData = '';
                this.content = '';

            },

            getCollection(val) {
                if (val)
                    Object.assign(this.jsonData, val)
            },

            closeHandler() {
                const title = this.title
                if (this.selection.search('Chart') !== -1 && this.file) {
                    const keys = Object.keys(this.jsonData[0])
                    const chartData = this.jsonData.map(e => e[keys[1]])
                    const chartLabels = this.jsonData.map(e => e[keys[0]])

                    const componentName = this.selection
                    const index = this.index
                    this.$emit('selections', {componentName, chartData, chartLabels, index, title})
                } else if (this.selection.search('Free Editor') !== -1) {
                    const componentName = 'Editor'
                    const title = this.title
                    const data = this.content
                    const index = this.index
                    console.log({data, index, title, componentName})
                    this.$emit('toEditor', {data, index, title, componentName})

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
