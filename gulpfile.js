var source = require("vinyl-source-stream");
var gulp = require('gulp');
var sass = require('gulp-ruby-sass');

// Sources
var src = {
    sass: 'static/sass/',
    scss: 'static/sass/**/*.scss',
}

gulp.task('sass', function() {
    return sass(src.sass, { style: 'expanded' })
        .pipe(gulp.dest('./static/css/'));
});


gulp.task('watch', function () {
    var watcher_sass = gulp.watch('./static/sass/**/*.scss', ['sass']);
    watcher_sass.on('change', function(event) {
        console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
});
