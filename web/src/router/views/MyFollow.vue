<template>
    <Follow></Follow>
</template>
<script>

    import Follow from "../../components/Shared/Follow";
    import store from "../../store/store";
    import reportService from "../../service/reportService";
    export default {
        name: 'MyFollow',
        components: {Follow},
        data: () => ({}),
        beforeDestroy() {
            store.commit('report/resetState');
        },
        beforeRouteEnter(to, from, next) {
            const user = store.state.auth.username
            reportService.GET_SUBSCRIBED_REPORTS({user})
            next()
        },

    }

</script>
