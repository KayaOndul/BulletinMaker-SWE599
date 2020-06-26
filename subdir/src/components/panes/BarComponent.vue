<script>
    import {Bar} from 'vue-chartjs'
    import Constants from '../../assets/constants'
    export default {
        extends: Bar,
        props: {

            chartData: {
                type: Object,
                required: false
            },
            chartLabels: {
                type: Array,
                required: true
            }
        },
        data() {
            return {
                options:Constants.barOptions
            }
        },

        methods: {
            renChart() {
                this.renderChart({
                    labels: this.chartLabels,
                    datasets: [
                        {
                            label: 'downloads',
                            borderColor: '#249EBF',
                            pointBackgroundColor: 'white',
                            borderWidth: 1,
                            pointBorderColor: '#249EBF',
                            backgroundColor: 'transparent',
                            data: this.chartData.data
                        }
                    ]
                }, this.options)
            }
        },
        mounted() {
            this.renChart()
        },


    }

</script>