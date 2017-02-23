require 'parallel'
require 'open3'

results = Parallel.map(1..100, in_threads: 4) {
	i, o, e = Open3::popen3("python #{ARGV[0]} < #{ARGV[1]}")
	
	[o.read, e.read]
}

res = results.max_by { |x| x[1] }

puts res[0]
STDERR.puts res[1]
