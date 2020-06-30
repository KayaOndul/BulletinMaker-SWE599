<template>
    <follow/>
</template>
<script>
    import Follow from "../../components/Shared/Follow";
    import store from "../../store/store";
    import reportService from "../../service/reportService";
    export default {
        components: {Follow},
        beforeDestroy() {
            store.commit('report/resetState');
        },
        beforeRouteEnter(to, from, next) {
            const user = to.params.username
            reportService.GET_SUBSCRIBED_REPORTS({user})
            next()
        },
    }


</script>
