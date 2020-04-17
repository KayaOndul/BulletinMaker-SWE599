<template>
    <div id="app">

        <br/>

        <div class="d-flex justify-content-between">
            <v-checkbox v-for="item in layout" :key="item.i" v-model="item.show" :label="item.title"></v-checkbox>
        </div>


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
        >


            <grid-item v-for="item in layout" :key="item.i"
                       :x="item.x"
                       :y="item.y"
                       :w="item.w"
                       :h="item.h"
                       :i="item.i">
                <div class="d-flex justify-content-end align-content-end">
                    <v-btn icon @click="()=>addPane(item.i)">
                        <v-icon>mdi-plus</v-icon>
                    </v-btn>
                    <SelectChartButton :index="item.i" @selections="changeChartHandler"/>
                    <v-btn icon @click="()=>removePane(item.i)">
                        <v-icon>mdi-trash-can-outline</v-icon>
                    </v-btn>

                </div>
                <template>
                    <component class="wrapper chartComponent" v-if="item.show===true&&item.component"
                               :is="item.component"
                               :chartLabels="item.chartLabels" :chartData="item.chartData"
                    ></component>
                </template>

            </grid-item>

        </grid-layout>

    </div>


</template>


<script>


    import {GridLayout, GridItem} from 'vue-grid-layout'
    import LineComponent from "@/components/LineComponent";
    import BarComponent from "@/components/BarComponent";
    import EmptyPane from "@/components/EmptyPane"
    import mockLayout from "@/mocks/mockLayout";
    import SelectChartButton from "@/components/SelectChartButton";

    export default {

        components: {
            GridLayout, GridItem, LineComponent, BarComponent, EmptyPane, SelectChartButton
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
            this.layout = mockLayout
        },


        methods: {
            addPane(index) {


                var refPane = this.layout.filter(e => index === parseInt(e.i))[0]
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
                lay.push({
                    "x": refPane.x, "y": refPane.y + 5, "w": 5, "h": 5, "i": iMax, component: 'EmptyPane', show: true

                })
                this.layout = lay
            },
            removePane(index) {
                this.layout = this.layout.filter(e => e.i !== index)
            },


            changeChartHandler(payload) {
                console.log(payload)
                var lay = Object.assign([], this.layout)
                lay = lay.map(e => {
                    if (e.i === payload.index) {
                        var retVal=Object.assign({},e)
                        retVal.component= payload.componentName === 'LineChart' ? 'LineComponent' : 'BarComponent'
                        retVal.chartLabels=payload.chartLabels
                        retVal.chartData.data=payload.chartData
                        return retVal
                    }
                    return e
                })
                this.layout = lay
            }

        }
    }

</script>

