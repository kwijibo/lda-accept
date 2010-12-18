require 'rexml/document'
include REXML
# file = File.new("bibliography.xml")
# doc = Document.new(file)
# puts doc

shared_examples_for "All XML Requests" do
    it "should have correct code and mimetype" do
     @response.code.should == 200
     @response.headers[:content_type].should == "application/xml"       
    end

    it "should report correct format and version" do 
       Document.new(@response.body).root.attributes['format'].should == "linked-data-api"
       Document.new(@response.body).root.attributes['version'].should == "0.2"
    end
    # 
    # it "should have a results object" do 
    #    query(@response, "$.result").should_not be_nil
    # end
    # 
    # it "should have a results object which is a hash" do 
    #  query(@response, "$.result").should be_an_instance_of(Hash)
    # end
    # 
    # it "should refer to its source" do 
    #  query(@response, "$.result._about").should_not be_nil
    # end
    # 
    # it "should refer to its API" do 
    #  query(@response, "$.result.isPartOf").should_not be_nil
    # end
    # 
    # it "should refer to its definition" do 
    #  query(@response, "$.result.definition").should_not be_nil
    # end

end

shared_examples_for "All XML List Endpoints" do
  
end