require File.join(File.dirname(__FILE__), "..", "helper/spec_helper.rb")

#Include shared_examples for JSON tests
require File.join( File.dirname(__FILE__), "..", "common/json_shared.rb")

#Include shared_examples for Education tests
require File.join( File.dirname(__FILE__), "edu_shared.rb")

describe "The Education API," do

 
  context "requesting the short view" do
    before :all do
        ENV['server'] ||= 'localhost'
        @response = server_get "education/api/schools.json?_view=short&_metadata=all"
    end
    
    it "should  list alternate views" do
      versions = []
      query(@response, "$.result.version").each { |version|
        versions.push(version['label'])
      }
      ["short","medium", "geo"].each{ |x| versions.should( include(x)) }
    end
    
    end
  
  
  
end