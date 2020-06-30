<template>
    <div>
        <v-spacer class="mt-6"/>
        <v-card-title class="primary white--text text-left display-1 font-italic">Followed By:</v-card-title>

        <v-card class=" d-flex flex-row flex-wrap">

            <div class="pa-2 " v-for="(person,idx) in profile.followed_by" :key="idx">
                <v-tooltip bottom light class=" teal primary--text">
                    <template v-slot:activator="{ on }">
                        <v-avatar @click="goToProfile(person)"
                                  size="5vh" v-on="on" class="clickable  primary mx-1">
                            <span class="white--text ">{{person[0]}}</span>
                        </v-avatar>
                    </template>
                    <span>{{person}}</span>
                </v-tooltip>

            </div>
        </v-card>
        <v-spacer class="mt-12"/>
        <v-card-title class="primary white--text text-left display-1 font-italic">Following:</v-card-title>
        <v-card class=" d-flex flex-row flex-wrap">

            <div class="pa-2 " v-for="(person,idx) in profile.followed_users" :key="idx">
                <v-tooltip bottom light class=" teal primary--text">
                    <template v-slot:activator="{ on }">
                        <v-avatar @click="goToProfile(person)"
                                  size="5vh" v-on="on" class="clickable  primary mx-1">
                            <span class="white--text ">{{person[0]}}</span>
                        </v-avatar>
                    </template>
                    <span>{{person}}</span>
                </v-tooltip>

            </div>
        </v-card>
    </div>
</template>

<script>
    import store from "../../store/store";
    import router from "../router";

    export default {
        name: 'FollowList',
        data() {
            return {}
        },
        methods: {

            goToProfile(username) {
                router.push({name: 'Profile', params: {username: username}})
            },
        },
        computed: {
            profile() {
                return store.state.search.profile ? store.state.search.profile : []
            }
        }
    }
</script>
