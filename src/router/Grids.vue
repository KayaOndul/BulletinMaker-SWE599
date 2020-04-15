<template>
    <div id="app" >

            <br/>

            <grid-layout
                    :layout="layout"
                    :col-num="12"
                    :row-height="30"
                    :is-draggable="true"
                    :is-resizable="true"
                    :is-mirrored="false"
                    :vertical-compact="true"
                    :margin="[10, 10]"
                    :use-css-transforms="true"
            >

                <grid-item v-for="item in layout" :key="item.i"
                           :x="item.x"
                           :y="item.y"
                           :w="item.w"
                           :h="item.h"
                           :i="item.i">
                    <line-component class="wrapper chartComponent"
                                    :chart-labels=" ['January', 'February', 'March', 'April', 'May', 'June', 'July']"
                                    :chart-data=" {
                                                      label: 'Data One',
                                                      backgroundColor: '#f87979',
                                                      data: [40, 39, 10, 40, 39, 80, 40]
                                                   }"
                                    ></line-component>
                </grid-item>
            </grid-layout>

        </div>

<!--    </div>-->
</template>


<script>
    var testLayout = [
        {"x":0,"y":0,"w":10,"h":10,"i":"0"},


    ];


    import {GridLayout, GridItem} from 'vue-grid-layout'
    import LineComponent from "@/components/LineComponent";

    export default {

        components: {
            GridLayout, GridItem, LineComponent
        }
        ,
        data() {
            return {
                layout: testLayout,
            }

        },
        mounted() {
            this.index = this.layout.length;
        },


        methods: {}
    }

</script>

