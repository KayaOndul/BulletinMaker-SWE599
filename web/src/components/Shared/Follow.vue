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


                <v-card-subtitle class="text-left">Subscribers:</v-card-subtitle>
                <div v-for="(person,idx) in card.subscribers" :key="idx">
                    <v-tooltip bottom light class=" teal primary--text">
                        <template v-slot:activator="{ on }">
                            <v-avatar @click="goToProfile(person)"
                                      size="3vh" v-on="on" class="clickable  accent mx-1">
                                <span class="white--text caption">{{badgeName(person)}}</span>
                            </v-avatar>
                        </template>
                        <span>{{person}}</span>
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
    import router from "../../router/router";
    import reportService from "../../service/reportService";
    import likeService from "../../service/likeService";
    import {mapGetters} from 'vuex'

    export default {
        name: 'Follow',
        components: {},
        data: () => ({}),


        watch: {},
        computed: {
            ...mapGetters({
                isLoggedIn: 'auth/isLoggedIn',
                reports: 'report/getReports'
            }),
             isOwner() {
                return store.state.auth.username ? false :
                    this.$route.params.username === store.state.auth.username
            }


        },


        methods: {
            likeReport(idx) {
                const model = 'report'
                const id = idx
                likeService.LIKE({model, id})
                    .then(() => this.getReports())
            },
            badgeName(username) {
                return username.split(' ').map(e => e.toUpperCase()[0]).join()
            },
            goToProfile(username) {
                router.push({name: 'Profile', params: {username: username}})
            },
            goToReport(id) {
                router.push({name: 'report', params: {id: id}})

            },
            getReports() {
                   let user
                if (this.isOwner) {
                    user = store.state.auth.username
                } else {
                    user = this.$route.params.username
                }

                reportService.GET_SUBSCRIBED_REPORTS({user})
            },
            pushHandlerCommunity(name) {
                this.$router.push(`/Community/${name}`)
            },
            randomColor() {

            }


        },

    }

</script>
