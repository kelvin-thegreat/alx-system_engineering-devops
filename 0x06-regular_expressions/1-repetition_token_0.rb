#!/usr/bin/env ruby

# Get the string argument from the command line
str = ARGV[0]

# Use a regular expression to match "hbn", "hbtn", "hbttn", "hbtttn", "hbttttn", "hbtttttn", or "hbttttttn"
if str =~ /hb[t]{0,6}n/
  puts "#{str}"
end
