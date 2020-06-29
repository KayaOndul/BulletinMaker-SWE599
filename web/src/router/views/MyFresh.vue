<template>
    <div class="d-flex flex-wrap mt-12">


        <v-card v-for="(card,index) in reports" :key="index" width="30vh" class=" mx-auto my-6"


        >
            <div @click="goToReport(card.id)"
                 class="d-flex clickable justify-space-between elevation-9 primary pa-3">
                <v-card-text class="d-inline-block text-wrap  white--text font-weight-bold "
                             v-text="`${card.title?card.title:'Unnamed Report'} `"/>

            </div>
            <v-img
                    @click="goToReport(card.id)"
                    :src="'https://picsum.photos/201'"

                    position="center"
                    class="clickable white--text mx-auto"
                    gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"


            >

                <template v-slot:placeholder>
                    <v-row
                            class="fill-height ma-0"
                            align="center"
                            justify="center"
                    >
                        <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                    </v-row>

                </template>

            </v-img>
            <div v-if="isLoggedIn" class="d-flex justify-end">
                <v-card-text class=" black--text text-left  "
                >by <span @click="goToProfile(card.owner)" class="clickable">{{card.owner}}</span></v-card-text>
                <v-tooltip bottom light class=" teal primary--text">
                    <template v-slot:activator="{ on }">
                        <v-btn @click="likeReport(card.id)" icon v-on="on">
                            <v-icon color="red">mdi-heart</v-icon>
                        </v-btn>
                    </template>
                    <span>Follow Report</span>
                </v-tooltip>
            </div>
            <v-card-actions class="d-flex flex-row  flex-wrap">

                <v-card-subtitle v-if="card.subscribers.length>0" class="text-left">Subscribers:</v-card-subtitle>
                <div v-for="(person,idx) in card.subscribers" :key="idx">
                    <v-tooltip bottom light class=" teal primary--text">
                        <template v-slot:activator="{ on }">
                            <v-avatar @click="goToProfile(person.username)"
                                      size="3vh" v-on="on" class="clickable  accent mx-1">
                                <span class="white--text caption">{{person.username[0].toUpperCase()}}</span>
                            </v-avatar>
                        </template>
                        <span>{{person.username}}</span>
                    </v-tooltip>

                </div>


            </v-card-actions>


        </v-card>
        <div v-if="reports&&reports.length<1">
            <v-card-title class="red--text display-2">Nothing Here!</v-card-title>
        </div>

    </div>
</template>
<script>
    import store from "../../store/store";
    import router from "../router";
    import reportService from "../../service/reportService";
    import {mapGetters} from 'vuex'
    import likeService from "../../service/likeService";

    export default {
        name: 'MyFresh',
        components: {},
        data: () => ({}),
        created() {

        },

        watch: {},
        computed: {
            ...mapGetters('auth', ['isLoggedIn']),
            reports: function () {
                return store.state.report.reports ? store.state.report.reports : []
            }
        },


        methods: {
            likeReport(idx) {
                const model = 'report'
                const id = idx
                likeService.LIKE({model, id})
                    .then(() => this.getReports())
            },
            goToProfile(username) {
                router.push({name: 'Profile', params: {username: username}})
            },
            goToReport(id) {
                router.push({name: 'report', params: {id: id}})

            },
            getReports() {

                reportService.GET_ALL_REPORTS()
            },
            pushHandlerCommunity(name) {
                this.$router.push(`/Community/${name}`)
            },
            randomColor() {

            },


        },
        beforeRouteEnter(to, from, next) {
            reportService.GET_ALL_REPORTS()
            next()
        },
        beforeDestroy() {
            store.commit('report/resetState');
        }
    }

</script>
