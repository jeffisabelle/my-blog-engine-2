var source = require("vinyl-source-stream");
var gulp = require('gulp');
var sass = require('gulp-ruby-sass');

gulp.task('sass', function() {
    return sass('./static/sass/**/*.scss', { style: 'expanded' })
        .pipe(gulp.dest('./static/css/'));
});


gulp.task('watch', function () {
    var watcher_sass = gulp.watch('./static/sass/**/*.scss', ['sass']);
    watcher_sass.on('change', function(event) {
        console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
});
