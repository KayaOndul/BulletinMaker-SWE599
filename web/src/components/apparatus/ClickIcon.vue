<template>
    <v-tooltip top light class="white primary--text clickable">
        <template v-slot:activator="{ on }">
            <v-btn icon v-on="on" @click="routeHandler">
                <v-icon class="primary--text">{{icono}}</v-icon>
            </v-btn>
        </template>
        <span class=" white--text">{{notto}}</span>
    </v-tooltip>
</template>

<script>
    import router from "../../router/router";
    import authService from "../../service/authService";
    import reportService from "../../service/reportService";
    import store from "../../store/store";

    export default {
        name: 'clickIcon',
        data() {
            return {}
        },
        props: ['note', 'icon', 'route'],
        components: {},
        computed: {
            notto() {
                return this.note ? this.note : ''
            },
            icono() {
                return this.icon ? this.icon : ''
            },
            routeo() {
                return this.route ? this.route : ''
            }

        },

        watch: {},

        mounted() {

        },
        methods: {
            routeHandler() {
                if (this.notto === 'Log Out') {
                    authService.LOGOUT()
                    this.$store.commit('global/set_alert', 'Logged Out')
                    this.$store.commit('report/resetState')
                    reportService.GET_ALL_REPORTS()
                    router.push({name: 'MyFresh'})
                }

                if (this.notto === 'Go To Your Profile' || this.notto === 'Dashboard') {
                    let route = {...this.routeo, params: {username: localStorage.getItem('username')}}
                    router.push(route)
                }
                if (this.notto === 'Create New Report') {

                    reportService.CREATE_REPORT()

                        .then(() =>
                            router.push({
                                name: 'report',
                                params:
                                    {id: store.state.report.reportNumber}
                            })
                        )

                }


                if (this.routeo) {
                    if (this.routeo.params) {
                        router.push({name: this.routeo.name, params: this.routeo.params})
                    } else {

                        router.push(this.routeo)
                    }
                }
            }

        }


    }
</script>

<style>

</style>
