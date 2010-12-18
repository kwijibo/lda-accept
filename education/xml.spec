require File.join(File.dirname(__FILE__), "..", "helper/spec_helper.rb")

#Include shared_examples for JSON tests
require File.join( File.dirname(__FILE__), "..", "common/xml_shared.rb")

#Include shared_examples for Education tests
require File.join( File.dirname(__FILE__), "edu_shared.rb")

describe "The Education API," do

  context "when accessing an unknown endpoint" do
    
    begin
      before :all do
      ENV['server'] ||= 'localhost'
      @response = server_get "fubar.xml"
      end
    rescue
      it "should report a 404 Not Found" do
       @response.code.should == 404       
      end
    end
  end
  
  context "when retrieving schools" do
    
    before :all do
    ENV['server'] ||= 'localhost'
    @response = server_get "education/api/schools.xml"
    end

    it_should_behave_like "All XML Requests"
    it_should_behave_like "All XML List Endpoints"      
         
  end

  context "when retrieving primary schools" do
    
    before :all do
    ENV['server'] ||= 'localhost'
    @response = server_get "education/api/schools/primary.xml"
    end

    it_should_behave_like "All XML Requests"
    it_should_behave_like "All XML List Endpoints"      

    
  end

  context "when retrieving secondary schools" do
    
    before :all do
    ENV['server'] ||= 'localhost'
    @response = server_get "education/api/schools/secondary.xml"
    end

    it_should_behave_like "All XML Requests"
    it_should_behave_like "All XML List Endpoints"      

  end
        
end
