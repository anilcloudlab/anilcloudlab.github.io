/* ---- Course Tab Switcher ---- */
function showCourseTab(tab, el) {
  // Hide all tabs
  document.querySelectorAll('.course-tab-content').forEach(function(t){ t.style.display = 'none'; });
  // Show selected
  var target = document.getElementById('ctab-' + tab);
  if (target) target.style.display = 'block';
  // Update pill active state
  if (el) {
    document.querySelectorAll('.cat-pill').forEach(function(p){ p.classList.remove('active'); });
    el.classList.add('active');
  } else {
    // Called programmatically (from card click) — find and activate pill
    document.querySelectorAll('.cat-pill').forEach(function(p){ p.classList.remove('active'); });
    document.querySelectorAll('.cat-pill').forEach(function(p){
      if (p.getAttribute('onclick') && p.getAttribute('onclick').indexOf("'" + tab + "'") > -1) {
        p.classList.add('active');
      }
    });
  }
  // Scroll to top of courses section
  var pg = document.getElementById('page-courses');
  if (pg) pg.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

/* ---- Course Download Modal ---- */
var _cdlCourseKey = 'devops';
var _cdlCourseName = 'DevOps Engineering';
var _cdlTitles = {
  devops: 'DevOps Engineering',
  multicloud: 'Multi-Cloud Engineering (AWS+Azure+GCP)',
  devsecops: 'DevSecOps Security Engineering',
  sre: 'SRE — Site Reliability Engineering'
};

function openCourseDownload(courseKey) {
  _cdlCourseKey = courseKey;
  _cdlCourseName = _cdlTitles[courseKey] || courseKey;
  document.getElementById('cdl-title').textContent = '📄 Download Curriculum — ' + _cdlCourseName;
  document.getElementById('cdl-course-key').value = courseKey;
  document.getElementById('cdl-course-name').value = _cdlCourseName;
  document.getElementById('courseDlMod').classList.add('show');
}

function handleCourseDl(e) {
  e.preventDefault();
  var name   = document.getElementById('cdl-name').value;
  var phone  = document.getElementById('cdl-phone').value;
  var email  = document.getElementById('cdl-email').value;
  var country= document.getElementById('cdl-country').value;
  var course = document.getElementById('cdl-course-name').value;
  var msg = '📄 *Curriculum Download Request — AnilCloudLab*\n\n'
    + 'Name: '    + name    + '\n'
    + 'Phone: '   + phone   + '\n'
    + 'Email: '   + email   + '\n'
    + 'Country: ' + country + '\n'
    + 'Course: '  + course  + '\n\n'
    + 'Please send me the full curriculum PDF. Thank you!';
  window.open('https://wa.me/917993822600?text=' + encodeURIComponent(msg), '_blank');
  document.getElementById('cdl-btn').textContent = '✅ Sent! Closing...';
  setTimeout(function(){
    document.getElementById('cdl-btn').textContent = '📄 Send Curriculum on WhatsApp';
    closeMod('courseDlMod');
    // Reset form
    document.getElementById('cdl-name').value  = '';
    document.getElementById('cdl-phone').value = '';
    document.getElementById('cdl-email').value = '';
    document.getElementById('cdl-country').value = '';
  }, 2000);
}

/* ---- Course Enroll Modal ---- */
function openCourseEnroll(courseName) {
  document.getElementById('ce-title').textContent = '🚀 Enroll — ' + courseName;
  document.getElementById('ce-course-name').value = courseName;
  document.getElementById('courseEnrollMod').classList.add('show');
}

function handleCourseEnroll(e) {
  e.preventDefault();
  var name   = document.getElementById('ce-name').value;
  var phone  = document.getElementById('ce-phone').value;
  var email  = document.getElementById('ce-email').value;
  var country= document.getElementById('ce-country').value;
  var bg     = document.getElementById('ce-bg').value;
  var course = document.getElementById('ce-course-name').value;
  var msg = '🎓 *New Enrollment — AnilCloudLab*\n\n'
    + 'Name: '       + name    + '\n'
    + 'Phone: '      + phone   + '\n'
    + 'Email: '      + email   + '\n'
    + 'Country: '    + country + '\n'
    + 'Course: '     + course  + '\n'
    + 'Background: ' + bg;
  window.open('https://wa.me/917993822600?text=' + encodeURIComponent(msg), '_blank');
  document.getElementById('ce-btn').textContent = '✅ Opening WhatsApp...';
  setTimeout(function(){
    document.getElementById('ce-btn').textContent = '🚀 Submit & Connect on WhatsApp';
    closeMod('courseEnrollMod');
    document.getElementById('ce-name').value    = '';
    document.getElementById('ce-phone').value   = '';
    document.getElementById('ce-email').value   = '';
    document.getElementById('ce-country').value = '';
    document.getElementById('ce-bg').value      = '';
  }, 2500);
}

