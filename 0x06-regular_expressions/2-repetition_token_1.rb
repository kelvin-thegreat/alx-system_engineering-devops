#!/usr/bin/env ruby

# Get the string argument from the command line
str = ARGV[0]

# Use a regular expression to find the first occurrence of "htn", "hbtn", "hbbtn", or "hbbbtn"
match = str.scan(/hb*tn/)

# Print the matching substring or an error message
match.each do |match|
  puts match
end
