<template>
    <div>
        <Layout>


            <v-card class="my-4"

                    color="primary"
                    dark
            >
                <div class="d-flex flex-no-wrap justify-space-between ">
                    <v-card-title class="headline"><strong>Welcome</strong></v-card-title>


                </div>

            </v-card>
            <v-container class="d-flex flex-wrap mt-12"
            >

                <v-card v-for="(card,index) in reports" :key="index" width="30vh" class=" mx-auto my-6"


                >
                    <div @click="goToReport(card.id)"
                         class="d-flex clickable justify-space-between elevation-9 primary pa-3">
                        <v-card-text class="d-inline-block text-wrap  white--text font-weight-bold "
                                     v-text="`${card.title?card.title:'Unnamed Report'} by ${card.owner}`"/>

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

                    <v-card-actions class="d-flex flex-row  flex-wrap">

                        <v-card-subtitle class="text-left">Subscribers:</v-card-subtitle>
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
            </v-container>
        </Layout>
    </div>
</template>

<script>

    import Layout from "../layouts/layout";
    import store from "../../store/store";
    import router from "../router";
    import reportService from "../../service/reportService";

    export default {
        name: 'Welcome',
        components: {Layout},
        data: () => ({}),
        created() {

        },
        mounted() {
            this.getReports()
        },
        watch: {},
        computed: {

            reports: function () {
                return store.state.report.reports ? store.state.report.reports : []
            }
        },


        methods: {
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

            }


        },
        beforeDestroy() {
            store.commit('report/resetState');
        }
    }

</script>
