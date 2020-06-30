<template>
    <div>
        <v-card>
            <v-card-subtitle class="text-left">Subscribers:</v-card-subtitle>
            <div v-for="(person,idx) in profile.followed_by" :key="idx">
                <v-tooltip bottom light class=" teal primary--text">
                    <template v-slot:activator="{ on }">
                        <v-avatar @click="goToProfile(person)"
                                  size="3vh" v-on="on" class="clickable  primary mx-1">
                            <span class="white--text caption">{{person[0].toUpperCase()}}</span>
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
    export default {
        name: 'FollowList',
        data() {
            return {}
        },
        computed: {
            profile() {
                return store.state.search.profile ? store.state.search.profile : []
            }
        }
    }
</script>
