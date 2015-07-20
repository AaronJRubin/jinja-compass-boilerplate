require 'filewatcher'

task :render do
  sh "python render.py"
end

task :compile_sass do
  sh "compass compile --sass-dir sass --css-dir build"
end

task :watch do
  FileWatcher.new(["templates/", "macros/", "sass/"]).watch do |filename|
    puts filename
    if filename.include? "scss"
      sh "rake compile_sass"
    elsif filename.include?("templates") or filename.include?("macros")
      sh "rake render"
    end
  end
end
