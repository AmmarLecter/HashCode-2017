require 'parallel'
require 'open3'

times = 1..100
testcases = ['me_at_the_zoo.in']

executions = times.zip(testcases.cycle)

results = Parallel.map(executions, in_threads: `cat /proc/cpuinfo | grep 'core id' | wc`.to_i) { |testcase|
	testcase = testcase[1]
	STDERR.puts testcase	
	i, o, e = Open3::popen3("python simannmain.py < #{testcase}")

	[testcase, o.read, e.read]
}

p results

res = results.group_by { |x| x[0] }.map { |key, val| val.max_by { |x| x[2] } }

res.each do |r|
	File.write("outs/#{r[0]}.out", r[1])
	File.write("outs/#{r[0]}.err", r[2])
end
