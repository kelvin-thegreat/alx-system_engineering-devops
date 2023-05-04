#!/usr/bin/env ruby

# Get the string argument from the command line
str = ARGV[0]

# Use a regular expression to match "hbn", "hbtn", "hbttn", "hbtttn", "hbttttn", "hbtttttn", or "hbttttttn"
matches = str.scan(/hb[t]{0,6}n/)

# Print all matches found
matches.each do |match|
  puts match
end
