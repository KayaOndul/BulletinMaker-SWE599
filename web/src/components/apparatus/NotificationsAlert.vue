<template>
    <v-container style="z-index: 3; position:absolute;right:0px;max-width: 50vh">
        <v-alert class="d-flex flex-column " v-for="(alert,index) in alerts" :key="index"
                 :type="conditions.some(el=>alert.includes(el))?'error':'success'"
                 mode="out-in"
                 transition="slide-x-reverse-transition"
                 dismissible
                 border="left"
                 elevation="2"
                 colored-border
                 :icon="conditions.some(el=>alert.includes(el))?'mdi-close-outline':'mdi-check-outline'"
        >
            {{alert}}

        </v-alert>


    </v-container>
</template>

<script>
    import _ from 'lodash'
    import store from "../../store/store";


    export default {
        data() {
            return {
                conditions:['400','401','402','403','404','405','406','500']
            }
        },

        computed: {


            alerts() {
                return store.state.global.alerts
            },


        },
        methods: {
            debounceRemove: _.debounce(function () {
                store.dispatch('global/removeAlert')
            }, 1500)
        },
        watch: {
            alerts(newVal) {
                if (newVal.length > 0) {
                    this.debounceRemove()
                }

            }
        },

    }
</script>
