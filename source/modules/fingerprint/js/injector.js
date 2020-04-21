
// Overwrite the `plugins` property to use a custom getter.
Object.defineProperty(navigator, "plugins", {
    get: () => new Array(Math.floor(Math.random() * 6) + 1),
});

// Pass the Webdriver test
Object.defineProperty(navigator, "webdriver", {
    get: () => false,
});

// hairline: store the existing descriptor
const elementDescriptor=Object.getOwnPropertyDescriptor(HTMLElement.prototype, "offsetHeight");

// redefine the property with a patched descriptor
Object.defineProperty(HTMLDivElement.prototype, "offsetHeight", {
    ...elementDescriptor,
    get: function() {
        if (this.id === "modernizr") {
            return 1;
        }
        return elementDescriptor.get.apply(this);
    },
});

["height", "width"].forEach(property => {
    // store the existing descriptor
    const imageDescriptor=Object.getOwnPropertyDescriptor(HTMLImageElement.prototype, property);

    // redefine the property with a patched descriptor
    Object.defineProperty(HTMLImageElement.prototype, property, {
        ...imageDescriptor,
        get: function() {
            // return an arbitrary non-zero dimension if the image failed to load
            if (this.complete && this.naturalHeight == 0) {
                return 16;
            }
            // otherwise, return the actual dimension
            return imageDescriptor.get.apply(this);
        },
    });
});

const getParameter=WebGLRenderingContext.getParameter;
WebGLRenderingContext.prototype.getParameter=function(parameter) {
    // UNMASKED_VENDOR_WEBGL WebGLRenderingContext.prototype.VENDOR
    if (parameter === 37445) {
        return "Google Inc.";
    }
    // UNMASKED_RENDERER_WEBGL WebGLRenderingContext.prototype.RENDERER
    if (parameter === 37446) {
        return "ANGLE (NVIDIA GeForce GTX 1050 Ti Direct3D11 vs_5_0 ps_5_0)";
    }
    return getParameter(parameter);
};
