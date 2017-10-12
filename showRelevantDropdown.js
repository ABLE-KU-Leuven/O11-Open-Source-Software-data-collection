function showRelevantFaculties(elem, restore) {
  $( ".program" ).css( "display", "none" );
  $( ".course" ).css( "display", "none" );
  selectedFaculty = "faculty"+ elem.value
  console.log(selectedFaculty)
  $( '#' + selectedFaculty ).css( "display", "inline" );
}

function showRelevantPrograms(elem, restore) {
  $( ".course" ).css( "display", "none" );
  selectedProgram = "program"+ elem.value
  console.log(selectedProgram)
  $( '#' + selectedProgram ).css( "display", "inline" );
}

function showRelevantCourses(elem, restore) {
  let selectedCourse = "course"+ elem.value
  $( ".submit" ).css( "display", "inline" );
  console.log(elem.value)
}

function getSelection(){

}

