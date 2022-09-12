


// Function grabs the nodeID
function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }), // Converts noteID to string
    }).then((_res) => {
      window.location.href = "/"; // Redirect to home page
    });
  }