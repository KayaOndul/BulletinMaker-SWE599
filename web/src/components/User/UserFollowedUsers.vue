<template>
  <v-card style="width: 100%">
        <v-data-table
                :headers="headers"
                :items="items"
                sort-by="calories"
                class="elevation-1"
                @click:row="clickHandler"
                style="cursor: pointer"
        >
            <template v-slot:top>
                <v-toolbar flat color="white">
                    <v-toolbar-title class="display-1">Anything You Follow or Create is Here</v-toolbar-title>
                    <v-divider
                            class="mx-4"
                            inset
                            vertical
                    ></v-divider>
                    <v-spacer></v-spacer>

                </v-toolbar>
            </template>
            <template v-slot:body="{ items }">
                <tbody>
                <tr class="text-left" v-for="item in items" :key="item.name">
                    <td @click="clickHandler(item)">{{ item.username }}</td>
                    <td v-if="showActions">
                        <div class="d-flex justify-start">
                            <FollowButton :item="item" :type-model="'userProfile'" />
                        </div>
                    </td>
                </tr>
                </tbody>
            </template>


            <template v-slot:no-data>
                <v-card-title>No Followed Users</v-card-title>
            </template>
        </v-data-table>
    </v-card>
</template>

<script>
    import store from "../../store/store";
    export default {
        data: () => ({
            dialog: false,
            headers: [
                {
                    text: 'Name',
                    align: 'start',
                    sortable: true,
                    value: 'username',
                },
                {
                    text: 'Type',
                    align: 'start',
                    sortable: true,
                    value: 'type',
                },
                {
                    text: 'Owner',
                    align: 'start',
                    sortable: true,
                    value: 'owner',
                },
                {text: 'Actions', value: 'actions', sortable: false},
            ],

        }),
        components:{},



        computed: {
            showActions() {

                if (localStorage.getItem('username') === this.$route.params.username) {
                    return true
                }
                return false
            },
            items(){
                return  store.state.global.visitedUserDetails?store.state.global.visitedUserDetails.followed_users:[]
            },
            formTitle() {
                return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
            },
        },

        watch: {
            dialog(val) {
                val || this.close()
            },
        },

        created() {

        },

        methods: {
            clickHandler(item){
                const username=item.username
                this.$router.push({name:'Profile',params:{username:username}})
            },

        },
    }
</script>
