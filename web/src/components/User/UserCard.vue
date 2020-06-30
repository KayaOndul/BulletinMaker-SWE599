<template>
    <v-card class="pa-3" style="text-align: left">


        <div class="d-flex justify-start align-center ">


        </div>

        <div class="d-flex justify-space-between ">
            <div class="d-flex flex-row">

                <div class="d-flex flex-column  align-center ">
                    <v-list-item-avatar
                            size="15vh" class="clickable  primary mx-1">
                        <span class="white--text display-3">{{badgeName()}}</span>
                    </v-list-item-avatar>
                </div>
                <div class="d-flex justify-center flex-column">
                    <v-card-title class="display-3"><strong>{{username}}</strong></v-card-title>
                </div>
                <div class="d-flex justify-center flex-column">
                    <v-card-title class="display-3"><strong>{{username}}</strong></v-card-title>
                </div>


            </div>


        </div>


    </v-card>


</template>

<script>

    import store from "../../store/store";
    export default {
        data() {
            return {}
        },
        components: {},
        methods: {

            badgeName() {
                return this.username.split(' ').map(e => e.toUpperCase()[0]).join()
            },

        },

        computed: {

            username() {
                return this.$route.params.username
            },
            profileData() {
                return store.state.search.profile ? store.state.search.profile : []
            }


        }

    }
</script>
