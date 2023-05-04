#!/usr/bin/env ruby
# A RegeX that matches 10 digit Phone Number
puts ARGV[0].scan(/^[0-9]{10}$/).join
