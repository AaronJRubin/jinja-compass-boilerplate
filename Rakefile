require 'filewatcher'

directory "build"

task :render => ["build"] do
  sh "python render.py"
end

task :compile_sass => ["build"] do
  sh "compass compile --sass-dir sass --css-dir build"
end

task :watch do
  FileWatcher.new(["templates/", "macros/", "sass/"]).watch do |filename| 
    if filename.include? "scss"
      sh "rake compile_sass"
    elsif filename.include?("templates") or filename.include?("macros")
      sh "rake render"
    end
  end
end
