# https://leetcode.com/problems/majority-element
# 169. Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# This solution uses Enum.reduce_while which creates a map with the count of all elements
# When an element with a count greater than ⌊n / 2⌋ is found, it halts and returns the element.

defmodule Solution do

  def majority_element([element]) do
    element
  end

  @spec majority_element(nums :: [integer]) :: integer
  def majority_element(nums) do
    target = div(length(nums), 2) # integer division

    Enum.reduce_while(nums, %{}, fn
      (value, map) ->
        # Update the map with the incremented count
        {count, map} = Map.get_and_update(map, value, fn
          (x) ->
            # Check x != nil
            if x do
              {x + 1, x + 1}
            else
              {1, 1}
            end
          end)

        if count > target do
          {:halt, value}
        else
          {:cont, map}
        end
    end)
  end
end

Solution.majority_element([2,2,1,1,1,2,2])
#Solution.majority_element([2])
|> IO.inspect()
#|> IO.puts()
