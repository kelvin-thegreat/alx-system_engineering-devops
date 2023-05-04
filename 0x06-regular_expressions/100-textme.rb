#!/usr/bin/env ruby

# Get the string argument from the command line
str = ARGV[0]

# Use a regular expression to find all matches of "School"
matches = str.scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/)

# Print all matches found
matches.each do |match|
  puts match.join(",")
end
