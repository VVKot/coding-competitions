class Solution {
  public String validateIPv4(String IP) {
    String[] nums = IP.split("\\.", -1);
    for (String x : nums) {
      if (x.length() == 0 || x.length() > 3) {
        return "Neither";
      }
      if (x.charAt(0) == '0' && x.length() != 1) {
        return "Neither";
      }
      for (char ch : x.toCharArray()) {
        if (!Character.isDigit(ch)) {
          return "Neither";
        }
      }
      if (Integer.parseInt(x) > 255) {
        return "Neither";
      }
    }
    return "IPv4";
  }

  public String validateIPv6(String IP) {
    String[] nums = IP.split(":", -1);
    String hexdigits = "0123456789abcdefABCDEF";
    for (String x : nums) {
      if (x.length() == 0 || x.length() > 4) {
        return "Neither";
      }
      for (Character ch : x.toCharArray()) {
        if (hexdigits.indexOf(ch) == -1) {
          return "Neither";
        }
      }
    }
    return "IPv6";
  }

  public String validIPAddress(String IP) {
    if (IP.chars().filter(ch -> ch == '.').count() == 3) {
      return validateIPv4(IP);
    } else if (IP.chars().filter(ch -> ch == ':').count() == 7) {
      return validateIPv6(IP);
    } else {
      return "Neither";
    }
  }
}
