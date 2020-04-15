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
                :margin="[30, 30]"
                :use-css-transforms="true"
        >

            <grid-item v-for="item in layout" :key="item.i"
                       :x="item.x"
                       :y="item.y"
                       :w="item.w"
                       :h="item.h"
                       :i="item.i">
                <template>
                    <component  class="wrapper chartComponent" v-if="item.show===true&&item.component" :is="item.component"
                      :chartLabels="item.chartLabels" :chartData="item.chartData"
                    ></component>
                    <div v-else v-html="item.component"></div>
                </template>

            </grid-item>

        </grid-layout>

    </div>


</template>


<script>


    import {GridLayout, GridItem} from 'vue-grid-layout'
    import LineComponent from "@/components/LineComponent";
    import BarComponent from "@/components/BarComponent";
    import mockLayout from "@/mocks/mockLayout";

    export default {

        components: {
            GridLayout, GridItem, LineComponent, BarComponent
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
               this.layout=mockLayout
        },


        methods: {}
    }

</script>

