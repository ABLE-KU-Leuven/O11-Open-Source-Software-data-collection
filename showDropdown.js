d3.json("options.json", function(data) {
    // Dropdowns 

    let input = data;

    d3.select('#faculties')
        .on('change', showPrograms);   
    
    d3.select('#programs')
        .on('change', showCourses);

    d3.select('#courses')
        .on('change', showSubmit);
    
    d3.select('#faculties')
        .selectAll('option')
        .data(data)
        .enter()
        .append('option')
            .text(function (d) { 
                return d.name; 
            })
            .each(function(d) {
                if (d.name === "Kies") {
                  d3.select(this).property("disabled", true)
                }
            });
    

    

    
    
    function showPrograms(d) {
        $( ".courses" ).css( "display", "none" );
        $( ".programs" ).css( "display", "none");
        selectedFaculty = d3.select('#faculties')[0][0].value
        programsData = findProgram(selectedFaculty)
        let programs = d3.select('#programs')
            .selectAll('option')
            .data(programsData)
            .enter()
            .append('option')
                .text(function (d) { 
                    return d.name; 
                });
        $( ".programs" ).css( "display", "inline" );
    };

    function showCourses(d) {
        $( ".courses" ).css( "display", "none" );
        selectedProgram = d3.select('#programs')[0][0].value
        coursesData = findCourses(selectedProgram)
        let courses = d3.select('#courses')
            .selectAll('option')
            .data(coursesData)
            .enter()
            .append('option')
                .text(function (d) { 
                    return d.name; 
                });
        $( ".courses" ).css( "display", "inline" );
        
    };

    function showSubmit() {
        selectedProgram = d3.select('#courses')[0][0].value
        $( ".submit" ).css( "display", "inline" );
    };

    function findProgram(facultyName){
        for(var i = 0; i < data.length; i++) {
            var faculty = data[i];
            if (faculty.name == facultyName){
                return faculty.children
            }
        }
    }

    function findCourses(courseName){
        for(var i = 0; i < data.length; i++) {
            var faculty = data[i];
            if (faculty.children != undefined){
                children = findCourses1(faculty.children, courseName)
                if (children != undefined){
                    return children
                }
            }   
        }
    }

    function findCourses1(programs, courseName){
        for(var i = 0; i < programs.length; i++) {
            var program = programs[i];
            if (program.name == courseName){
                return program.children
            }
        }
    }


    
});