    // DataTable for table search
      // Staff table
    $(document).ready(function() {
        $('#staff_table').DataTable({
        "pageLength": 3,
        "paging": true,
        "lengthChange": true,
        "searching": true,
        "ordering": true,
        "info": true,
        "autoWidth": true
            });
        } );

    // Patient table
    $(document).ready(function() {
        $('#patient_table').DataTable({
        "pageLength": 3,
        "paging": true,
        "lengthChange": true,
        "searching": true,
        "ordering": true,
        "info": true,
        "autoWidth": true
            });
        } );

   // Civility table
    $(document).ready(function() {
    $('#civility_table').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );    

    // Gender table
    $(document).ready(function() {
    $('#gender_table').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );        

     // Treatment status table
    $(document).ready(function() {
    $('#status-table').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );  

 // Staff role table
    $(document).ready(function() {
    $('#position-table').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );    

     // patient for appointment table
    $(document).ready(function() {
    $('#patient_for_appointment').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );   
    
     // Bills list table
    $(document).ready(function() {
    $('#treatmentBill').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );   
    
     // patient for treatment table

    $(document).ready(function() {
    $('#patient_for_treatment').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );


    // blood group table

    $(document).ready(function() {
    $('#bg_table').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );


    // departments  table

    $(document).ready(function() {
    $('#dp_table').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );

   
    // companies  table

    $(document).ready(function() {
    $('#cp_table').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } ); 

    // Faqs  table
    $(document).ready(function() {
    $('#faq_table').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } ); 


    // interventions
    $(document).ready(function() {
    $('#intervention_table').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );

    //insurance_table 
    $(document).ready(function() {
    $('#insurance_table').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );    

   //appointmentList_table 
    $(document).ready(function() {
    $('#appointmentList').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );    

       //treatmentList_table 
    $(document).ready(function() {
    $('#treatmentList').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );    


    //Interventions
    $(document).ready(function() {
    $('#interventionList').DataTable({
    "pageLength": 3,
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true
        });
    } );    

    


/*
   
$(document).ready(function(){
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
            }
        }
    });

});

*/

