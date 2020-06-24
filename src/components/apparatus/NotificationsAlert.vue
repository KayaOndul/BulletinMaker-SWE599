<template>
    <v-container style="z-index: 3; position:absolute;right:0px">
            <v-alert class="d-flex flex-column "   v-for="(alert,index) in alerts" :key="index"
                     :type="'error'"
                    mode="out-in"
                    transition="slide-x-reverse-transition"
                    dismissible
                    border="left"
                    elevation="2"
                    colored-border
                    :icon="!alert.status?'mdi-close':'mdi-check'"
            >
                {{alert.detail}}
<!--                {{!alert.status?'':alert.status}}  {{alert.statusText?alert.statusText:''}} {{alert.detail?alert.detail:''}}-->
            </v-alert>


    </v-container>
</template>

<script>
    import _ from 'lodash'
    import store from "../../store/store";


    export default {
        data() {
            return {}
        },

        computed: {


            alerts() {
                return store.state.global.alerts
            },


        },
        methods: {
            debounceRemove: _.debounce(function () {
                store.dispatch('global/removeAlert')
            }, 1000)
        },
        watch: {
            alerts(newVal) {
                if (newVal.length > 0){
                    this.debounceRemove()
                }

            }
        },

    }
</script>