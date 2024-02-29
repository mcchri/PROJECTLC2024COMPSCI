<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Firebase Data Chart</title>
    <script type="module" src="https://cdn.jsdelivr.net/npm/chart.js@3.7.0/dist/chart.min.js"></script>
</head>
<body>
    <h1>Firebase Data Chart</h1>
    <div>
        <canvas id="dataChart"></canvas>
    </div>

    <script type="module">
        import { initializeApp } from "https://www.gstatic.com/firebasejs/10.4.0/firebase-app.js";
        import { getDatabase, ref, onChildAdded } from "https://www.gstatic.com/firebasejs/10.4.0/firebase-database.js";

        const firebaseConfig = {
            apiKey: "AIzaSyBc8kckOZJK6SWu9l2wTdu_0670eeZD0dE",
            authDomain: "comp-sci-c8d0a.firebaseapp.com",
            databaseURL: "https://YOUR_PROJECT_ID.firebaseio.com",
            databaseURL: "https://comp-sci-c8d0a-default-rtdb.europe-west1.firebasedatabase.app",
            projectId: "comp-sci-c8d0a",
            storageBucket: "comp-sci-c8d0a.appspot.com",
            messagingSenderId: "711439640173",
            appId: "1:711439640173:web:d818150868affc75844164",
            measurementId: "G-4RX0SVHZQE"
        };

        // Initialize Firebase
        const app = initializeApp(firebaseConfig);

        const db = getDatabase();

        const nodes = ['Level','Score','time_taken_at'];

        //const dataRefs = nodes.map(node => ref(db, node + '/').limitToLast(31));
        const dataRef = nodes.map(node => ref(db, node + '/'));

        const ctx = document.getElementById('dataChart').getContext('2d');
        const dataChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: nodes.map((node, index) => ({
                    label: node,
                    data: [],
                    borderColor: `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, 1)`,
                    borderWidth: 1,
                    fill: false
                }))
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    },
                    x: {
                        max: 30
                    }
                }
            }
        });

       /* dataRef.forEach((ref, index) => {
            onChildAdded(ref, (snapshot) => {
                const data = snapshot.val();
                var date = new Date(index.key * 1000)
                let mm = date.getMonth() + 1; // Months start at 0!
                let dd = date.getDate();
                let hr = date.getHours();
                let mn = date.getMinutes();
                let sc = date.getSeconds();
        
                if (dd < 10) dd = '0' + dd;
                if (mm < 10) mm = '0' + mm;
                if (mn < 10) mn = '0' + mn;
        
                const formatteddate = dd + '_' + mm + ' ' + hr +':'+ mn +':'+ sc;
                
                const timestamp = snapshot.key;
                const value = parseInt(data[Object.keys(data)[0]]);
                
                if (value > 0){
                  
                dataChart.data.labels.push(formatteddate);
                dataChart.data.datasets[index].data.push(value);
                dataChart.update();
                }
                
            });
        }); */
        dataRef.forEach((ref, index) => {
    onChildAdded(ref, (snapshot) => {
        const data = snapshot.val();
                var date = new Date(snapshot.key *1000)
                let mm = date.getMonth() + 1; // Months start at 0!
                let dd = date.getDate();
                let hr = date.getHours();
                let mn = date.getMinutes();
                let sc = date.getSeconds();
        
                if (dd < 10) dd = '0' + dd;
                if (mm < 10) mm = '0' + mm;
                if (mn < 10) mn = '0' + mn;
        
                const formatteddate = dd + '_' + mm + ' ' + hr +':'+ mn +':'+ sc;
      
        const timestamp = snapshot.key;
        const value = parseInt(data[Object.keys(data)[index]]); // Adjust this according to your data structure
        
        // Format timestamp as needed
        
        
        // Ensure the value is valid before adding to the chart
        if (!isNaN(value) && value > 0 && value < 100) {
            console.log(value)
            var now = new Date();
            dataChart.data.labels.push(formatteddate);
            if (dataChart.data.datasets[index].data.length > 30) {
                dataChart.data.labels.shift();
                dataChart.data.datasets[index].data.shift();
            }
            
                dataChart.data.datasets[index].data.push(value); // Remove the first entry if more than 30
                dataChart.update(); // Remove the corresponding label
        
            
        }
        
    });
});
    </script>
</body>
</html>
