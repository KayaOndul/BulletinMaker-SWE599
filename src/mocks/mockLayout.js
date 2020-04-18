export default [
    {
        "x": 0, "y": 0, "w": 5, "h": 5, "i": 0, component: 'LineComponent',
        title: 'LineChart',
        isComponent: true,
        chartLabels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        chartData: {
            label: 'Data One',
            backgroundColor: '#f87979',
            pointBackgroundColor: 'white',
            borderWidth: 1,
            pointBorderColor: '#249EBF',
            data: [40, 20, 30, 50, 90, 10, 20, 40, 50, 70, 90, 100]
        }
    },
    {
        "x": 0, "y": 2, "w": 5, "h": 5, "i": 1, component: 'BarComponent',
        title: 'BarChart',
        isComponent: true,
        chartLabels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        chartData: {
            label: 'Data One',
            backgroundColor: '#f87979',
            pointBackgroundColor: 'white',
            borderWidth: 1,
            pointBorderColor: '#249EBF',
            data: [40, 20, 30, 50, 90, 10, 20, 40, 50, 70, 90, 100]
        }
    }
]