rule '.md' => '.Rmd' do |t|
  sh "Rscript -e \"library(knitr); knit('#{t.source}')\""
end

rule '.pdf' => '.md' do |t|
  sh "pandoc -f markdown+inline_notes -V geometry:margin=1in --highlight-style tango #{t.source} -o #{t.name}"
end

commands = ['python', 'python3', 'pypy', 'jython', 'ipy']

task :eulertest do
  commands.each do |command|
    sh "#{command} python/eulertest.py > #{command}.results.txt"
  end
end

file 'results.txt' => commands.map { |c| "#{c}.results.txt" } do |t|
  File.open(t.name, 'w') do |f|
    f.write(commands.join("\t") + "\n")
    lines = commands.map { |c| File.open("#{c}.results.txt").readlines }
    lines[0].zip(*lines[1..-1]).each do |l|
      f.write(l.map{ |x| x.split()[-1] }.join("\t") + "\n")
    end
  end
end
