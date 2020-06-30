<template>
    <v-card class="my-4"

            color="primary"
            dark
    >
        <div class="d-flex flex-no-wrap justify-space-between ">
            <v-card-title class="headline">{{name}}</v-card-title>


        </div>

    </v-card>
</template>

<script>
    export default {
        name:'Header',
        data(){
            return{

            }
        },
        props:['name']
    }
</script>
