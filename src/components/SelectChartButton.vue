<template>

    <v-dialog v-model="dialog" persistent max-width="600px">
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
                        <v-col cols="8">
                            <v-text-field label="Title*" type="text" required></v-text-field>
                            <v-select
                                    v-model="selection"
                                    :items="chartTypes"
                                    label="Select a type*"
                                    required
                            ></v-select>
                        </v-col>

                        <v-col cols="8" v-if="selection!==''">
                            <input type="file" @change="onChange"/>
                            <xlsx-read :file="file">
                                <xlsx-json @parsed="getCollection">
                                    <template #default="{collection}">
                                        <div>
                                            {{ collection }}
                                        </div>
                                    </template>
                                </xlsx-json>
                            </xlsx-read>
                        </v-col>


                    </v-row>
                </v-container>
                <small>*indicates required field</small>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
                <v-btn color="blue darken-1" text @click="dialog = false">Save</v-btn>
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
            file: null,
            jsonData: {},

        }),
        methods: {
            onChange(event) {
                this.file = event.target.files ? event.target.files[0] : null;
            },
            getCollection(val) {
                if (val)
                    Object.assign(this.jsonData,val)
            }

        },
        computed: {
            chartTypes() {
                return Constants.chartTypes ? Constants.chartTypes : []
            },
        },
        watch: {
            selection(newVal) {
                if (newVal !== '') {
                    this.$emit('selection', newVal)
                }
            },

        }
    }
</script>