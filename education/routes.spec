require File.join(File.dirname(__FILE__), "..", "helper/spec_helper.rb")

#Include shared_examples for JSON tests
require File.join( File.dirname(__FILE__), "..", "common/json_shared.rb")
require File.join( File.dirname(__FILE__), "..", "common/xml_shared.rb")

#Include shared_examples for Education tests
require File.join( File.dirname(__FILE__), "edu_shared.rb")

describe "The Education API," do

  context "when accessing the schools endpoint" do
    
    begin
      before :all do
      ENV['server'] ||= 'localhost'
      @response = server_get "education/api/schools"
      end
      it "should return a 200 OK" do
       @response.code.should == 200       
      end
    end
  
  end
  
  context "when accessing the primary schools endpoint" do
    
  begin
        before :all do
        ENV['server'] ||= 'localhost'
        @response = server_get "education/api/schools/primary"
        end
        it "should return a 200 OK" do
          @response.code.should == 200       
        end
    end
  end
  # 
  context "when accessing the secondary schools endpoint" do
    
      before :all do
      ENV['server'] ||= 'localhost'
      @response = server_get "education/api/schools/secondary"
      end
      
      it "should return a 200 OK" do
       @response.code.should == 200             
      end
    end
  # 
  context "when accessing the  primary schools by district endpoint" do
    
    begin
      before :all do
      ENV['server'] ||= 'localhost'
      @response = server_get "education/api/schools/primary/district/Westminster"
      end
      
      it "should return a 200 OK" do
       @response.code.should == 200       
      end
    end
  
  
  end
  
  
  context "when accessing the  secondary schools by district endpoint" do
  
       before :all do
       ENV['server'] ||= 'localhost'
       @response = server_get "education/api/schools/secondary/district/Westminster"
       end
       it "should return a 200 OK" do
        @response.code.should == 200       
       end
      end    
end