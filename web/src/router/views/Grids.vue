<template>
    <div id="app">
        <v-spacer class="ma-12"/>
        <v-toolbar class="ma-auto" style="width: 50%">
            <v-toolbar-title class="accent--text title  mr-3 font-weight-bold">Report Menu</v-toolbar-title>
            <v-spacer/>
            <v-list-item-group>
                <v-list-item v-if="this.layout.length<1">
                    <v-tooltip bottom light class="teal primary--text">
                        <template v-slot:activator="{ on }">
                            <v-btn @click="addEmptyPane" icon v-on="on" >
                                <v-icon>mdi-plus</v-icon>
                            </v-btn>
                        </template>
                        <span>Add Pane</span>
                    </v-tooltip>

                </v-list-item>
            </v-list-item-group>

        </v-toolbar>

        <grid-layout
                :layout="layout"
                :col-num="12"
                :row-height="30"
                :is-draggable="true"
                :is-resizable="true"
                :is-mirrored="false"
                :vertical-compact="true"
                :margin="[50, 50]"
                :use-css-transforms="true"
                :autoSize="true"

        >


            <grid-item v-for="item in layout" :key="item.i"
                       :x="item.x"
                       :y="item.y"
                       :w="item.w"
                       :h="item.h"
                       :i="item.i"


            >

                <div class="d-flex justify-content-end align-content-end">
                    <v-btn icon @click="()=>addPane(item.i)">
                        <v-icon>mdi-plus</v-icon>
                    </v-btn>
                    <SelectChartButton v-if="item.component=='EmptyPane'" :index="item.i"
                                       @selections="changeChartHandler"
                                       @toEditor="editorHandler"


                    />
                    <v-btn icon @click="()=>removePane(item.i)">
                        <v-icon>mdi-trash-can-outline</v-icon>
                    </v-btn>
                    <h3 class=" accent--text pl-3" v-show="item.title!==''">{{item.title}}</h3>

                </div>

                <template>
                    <component class="wrapper chartComponent" v-if="!item.data&&item.isComponent===true"
                               :is="item.component"
                               :chartLabels="item.chartLabels" :chartData="item.chartData"
                    ></component>
                    <component class="wrapper chartComponent px-3 " style="padding-bottom: 1vh"
                               v-else-if="item.isComponent===true"
                               :is="item.component"
                               v-model="layout.filter(e=>e.i===item.i)[0].value"

                    ></component>

                </template>


            </grid-item>

        </grid-layout>


    </div>


</template>


<script>

    import {GridItem, GridLayout} from 'vue-grid-layout'
    import LineComponent from "@/components/panes/LineComponent";
    import BarComponent from "@/components/panes/BarComponent";
    import {VueEditor} from 'vue2-editor'
    import EmptyPane from "@/components/panes/EmptyPane"
    import mockLayout from "@/mocks/mockLayout";
    import SelectChartButton from "@/components/panes/SelectChartButton";
    import Constants from '../../assets/constants'

    export default {
        name: 'Grids',
        components: {
            GridLayout, GridItem, LineComponent, BarComponent, EmptyPane, SelectChartButton, VueEditor
        }
        ,
        data() {
            return {
                layout: [],
                checkBoxLineChart: false,
                checkBoxBarChart: false,

            }

        },
        mounted() {
            this.layout = mockLayout.slice(0)
        },


        methods: {

            addPane(index) {

                //Find the referenced pane
                var refPane=this.layout.filter(e => index === parseInt(e.i))[0]

                //Calculate index form the pane to be inserted
                var iMax = this.layout.map(a => a.i).reduce((a, b) => {
                    return Math.max(a, b)
                }) + 1

                var lay = this.layout.map(e => {
                    if (e["x"] === refPane.x && e["i"] !== index) {
                        return {
                            ...e,
                            " y": e.y + 5
                        }
                    }
                    return e;

                })
                var dummy = Constants.template
                dummy = {
                    ...dummy,
                    "x": refPane ? refPane.x : 0,
                    "y": refPane ? refPane.y + 5 : 0,
                    "w": 5,
                    "h": 8,
                    "i": iMax,
                    component: 'EmptyPane',
                    show: true
                }
                lay.push(dummy)
                this.layout = lay
            },
            removePane(index) {
                this.layout = this.layout.filter(e => e.i !== index)
            },
            addEmptyPane(){
                this.layout.push(mockLayout[0])
            },

            changeChartHandler(payload) {
                console.log(payload)
                let lay = Object.assign([], this.layout);
                lay = lay.map(e => {
                    if (e.i === payload.index) {
                        var retVal = Object.assign({}, e)
                        retVal.isComponent = true
                        retVal.component = payload.componentName === 'LineChart' ? 'LineComponent' : 'BarComponent'
                        retVal.chartLabels = payload.chartLabels
                        retVal.chartData.data = payload.chartData
                        retVal.title = payload.title

                        return retVal
                    }

                    return e
                })
                this.layout = lay
            },

            editorHandler(payload) {
                console.log(payload)
                let lay = Object.assign([], this.layout);
                lay = lay.map(e => {
                    if (e.i === payload.index) {
                        var retVal = Object.assign({}, e)
                        retVal.data = payload.data ? payload.data : "<h1>waiting for new content</h1>"
                        retVal.isComponent = true
                        retVal.component = 'VueEditor'
                        retVal.title = payload.title
                        return retVal
                    }
                    return e
                })
                this.layout = lay
            },


        }
    }

</script>

