
require 'test/unit'
require_relative 'utils'
#load 'utils.rb'

class TC_PasswordTest < Test::Unit::TestCase

  def test_is_prime
    assert(!is_prime(0), 'zero is not prime')
    assert(!is_prime(1), 'one is not prime')
    assert(is_prime(2))
    assert(is_prime(3))
    assert(!is_prime(4))
  end

end
