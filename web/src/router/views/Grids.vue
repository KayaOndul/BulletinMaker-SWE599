<template>
    <div id="app">
        <layout>
            <v-spacer class="ma-12"/>

            <v-toolbar class="ma-auto" style="width: 70%">
                <v-toolbar-title class="accent--text title  mr-3 font-weight-bold">Report Menu</v-toolbar-title>


                <v-list-item-group>
                    <v-list-item>
                        <v-text-field v-model="title"

                                      :disabled="!this.isOwner"
                                      dense
                                      class=" mt-2"
                                      label="Report Title">

                        </v-text-field>
                    </v-list-item>
                </v-list-item-group>
                <v-spacer/>
                <v-list-item-group v-if="isOwner" class="d-flex text-no-wrap">
                    <v-spacer/>

                    <v-list-item v-if="this.layout?this.layout.length<1:false">
                        <v-tooltip bottom light class="teal primary--text">
                            <template v-slot:activator="{ on }">
                                <v-btn @click="addEmptyPane(0)" icon v-on="on">
                                    <v-icon>mdi-plus</v-icon>
                                </v-btn>
                            </template>
                            <span>Add Pane</span>
                        </v-tooltip>
                    </v-list-item>
                    <v-list-item>
                        <v-tooltip bottom light>
                            <template v-slot:activator="{ on }">
                                <v-btn @click="deleteLayout" icon v-on="on"
                                       class="colorHandler">
                                    <v-icon>
                                        mdi-trash-can-outline
                                    </v-icon>
                                </v-btn>
                            </template>
                            <span>Delete Layout</span>
                        </v-tooltip>
                    </v-list-item>
                    <v-list-item>
                        <v-tooltip bottom light>
                            <template v-slot:activator="{ on }">
                                <v-btn @click="saveLayout" icon v-on="on"
                                       class="colorHandler">
                                    <v-icon>
                                        mdi-content-save
                                    </v-icon>
                                </v-btn>
                            </template>
                            <span>Save Layout</span>
                        </v-tooltip>
                    </v-list-item>
                </v-list-item-group>
                <v-list-item-group v-if="!isOwner">
                    <div v-if="isLoggedIn===true" class="d-flex justify-end">
                        <v-tooltip bottom light class=" teal primary--text">
                            <template v-slot:activator="{ on }">
                                <v-btn @click="likeReport" icon v-on="on">
                                    <v-icon :color="isSubscriber===true?'red':'black'">mdi-heart</v-icon>
                                </v-btn>
                            </template>
                            <span>{{isSubscriber===true?'Unfollow Report':'Follow Report'}}</span>
                        </v-tooltip>
                    </div>
                </v-list-item-group>

            </v-toolbar>


            <grid-layout
                    :layout="layout?layout:[]"
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


                <grid-item v-for="(item) in layout" :key="item.i"
                           :x="item.x"
                           :y="item.y"
                           :w="item.w"
                           :h="item.h"
                           :i="item.i"


                >

                    <div v-if="isOwner==true" class="d-flex justify-content-end align-content-end">
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
                                   v-else
                                   :grid-index="item.i"
                                   :received-content="item.data"
                                   @changed="changeHandler"
                                   :is="item.component"


                        ></component>

                    </template>


                </grid-item>

            </grid-layout>
        </layout>

    </div>


</template>


<script>
    import layout from "../layouts/layout";
    import {GridItem, GridLayout} from 'vue-grid-layout'
    import LineComponent from "@/components/panes/LineComponent";
    import BarComponent from "@/components/panes/BarComponent";
    import EmptyPane from "@/components/panes/EmptyPane"
    import mockLayout from "@/mocks/mockLayout";
    import Editor from "../../components/panes/Editor"
    import SelectChartButton from "@/components/panes/SelectChartButton";
    import Constants from '../../assets/constants'
    import reportService from "../../service/reportService";
    import store from "../../store/store";
    import router from "../router";
    import {mapGetters} from 'vuex'

    const initState = () => {
        return {
            title: '',
            layout: [],
        }
    }
    import likeService from "../../service/likeService";

    export default {
        name: 'Grids',
        components: {
            GridLayout, GridItem, LineComponent, BarComponent, EmptyPane, SelectChartButton, Editor, layout
        }
        ,
        data() {
            return initState()
        },
        mounted() {
            this.layout = mockLayout.slice(0)
        },
        computed: {
            isSubscriber() {
                const uname = localStorage.getItem('username') ? localStorage.getItem('username') : ''

                return this.report.subscribers.filter(e => e === uname).length > 0
            },
            ...mapGetters('auth', ['isLoggedIn']),
            isOwner() {
                return store.state.auth.username === store.state.report.report.owner
            },
            report() {
                return store.state.report.report ? store.state.report.report : []
            },

        },
        watch: {

            report(newVal) {

                if (newVal.length < 1) {
                    this.clean()
                }
                if (newVal.layout) {
                    this.clean()
                    this.layout = newVal.layout
                    this.title = newVal.title
                }

            }


        },

        methods: {
            clean() {
                this.layout = mockLayout.slice(0)
                this.title = []
            },
            addPane(index) {

                //Find the referenced pane
                var refPane = this.layout.filter(e => index === parseInt(e.i))[0]

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
            addEmptyPane() {
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
                        retVal.component = 'Editor'
                        retVal.title = payload.title
                        return retVal
                    }
                    return e
                })
                this.layout = lay
            },

            changeHandler(val) {
                this.layout.filter(e => e.i === val.iAm)[0].data = val.newVal

            },
            saveLayout() {
                const layout = this.layout
                const title = this.title ? this.title : store.state.report.report.title ? store.state.report.report.title : ''
                const id = this.$route.params.id
                const payload = {layout, title, id}
                reportService.PATCH_REPORT(payload)
            },
            deleteLayout() {
                const id = this.$route.params.id

                reportService.DELETE_REPORT({id})
                    .then(() => router.push({name: 'MyReport'}))
            },
            likeReport() {
                const model = 'report'
                const id = store.state.report.report.id
                likeService.LIKE({model, id})
                    .then(() => reportService.GET_REPORT({id})
                    )
            },
        },
        beforeRouteEnter(to, from, next) {
            const id = to.params.id
            reportService.GET_REPORT({id})
            next()
        },
        beforeRouteLeave(to, from, next) {
            const id = store.state.report.report.id

            if (id && !store.state.report.report.layout&&this.isOwner) {
                reportService.DELETE_REPORT({id})
            }
            store.commit('report/resetState')
            next()
        }
    }

</script>

